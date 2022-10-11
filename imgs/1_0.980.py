d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.N, Length.long)
d.position_pen(1,3)

d.end()
