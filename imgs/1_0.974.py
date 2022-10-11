d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.short, Radius.high)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,0)

d.end()
