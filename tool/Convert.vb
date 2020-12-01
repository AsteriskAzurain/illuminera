Public Class Convert

    Public Shared Function ConvertToSWF(ByVal PDFsourcePath As String, ByVal SWFtargetPath As String) As Boolean

        Dim result As Boolean = True

        Dim convertToolPath As String = Application.StartupPath & "\..\..\tool\pdf2swf.exe"
        Dim fontPath As String = "Languagedir=" & Application.StartupPath & "\..\..\xpdf-chinese-simplified"

        Try
            Dim pro As Process = New Process()
            pro.StartInfo.FileName = "cmd"
            pro.StartInfo.UseShellExecute = False
            pro.StartInfo.RedirectStandardInput = True
            pro.StartInfo.RedirectStandardOutput = True
            pro.StartInfo.CreateNoWindow = True
            pro.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden
            pro.Start()
            Dim input As String = String.Format("{0} {1} -o {2} -t ", convertToolPath, PDFsourcePath, SWFtargetPath)
            pro.StandardInput.WriteLine(input)
            pro.StandardInput.WriteLine("exit")
            Dim output As String = pro.StandardOutput.ReadToEnd()
            pro.WaitForExit()
            pro.Close()
            result = True

        Catch
            result = False
        End Try
        Return result
    End Function
End Class
