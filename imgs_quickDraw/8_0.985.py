d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(0,0)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.N, Length.short)

d.end()
