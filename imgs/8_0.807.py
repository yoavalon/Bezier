d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.NE, Length.long)
d.position_pen(0,3)
d.straight_line(Direction.SE, Length.short)

d.end()
