d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)

d.end()
