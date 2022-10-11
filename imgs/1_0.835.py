d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
