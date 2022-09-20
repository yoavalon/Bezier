d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.short)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)

d.end()
