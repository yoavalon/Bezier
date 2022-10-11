d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)

d.end()
