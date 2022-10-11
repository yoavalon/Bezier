d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(0,3)
d.straight_line(Direction.W, Length.short)
d.position_pen(0,3)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(3,1)

d.end()
