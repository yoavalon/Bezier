d = DslBezier()

d.position_pen(2,2)
d.position_pen(1,3)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.short)

d.end()
